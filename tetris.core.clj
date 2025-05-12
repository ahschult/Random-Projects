(ns tetris.core
  (:require [clojure.math.numeric-tower :as math]))

;; Game constants
(def ^:const board-width 10)
(def ^:const board-height 20)

;; Tetromino shapes (relative coordinates)
(def shapes
  {:I [[0 0] [1 0] [2 0] [3 0]]
   :O [[0 0] [1 0] [0 1] [1 1]]
   :T [[0 0] [1 0] [2 0] [1 1]]
   :S [[0 1] [1 1] [1 0] [2 0]]
   :Z [[0 0] [1 0] [1 1] [2 1]]
   :J [[0 0] [0 1] [1 1] [2 1]]
   :L [[0 1] [1 1] [2 1] [2 0]]})

;; Initialize game state
(defn init-game []
  {:board (vec (repeat board-height (vec (repeat board-width 0))))
   :current-piece (rand-nth (vals shapes))
   :piece-position [4 0]
   :score 0})

;; Check if a position is valid
(defn valid-position? [board piece position]
  (let [[x y] position]
    (every? (fn [[dx dy]]
              (let [nx (+ x dx)
                    ny (+ y dy)]
                (and (<= 0 nx (dec board-width))
                     (<= 0 ny (dec board-height))
                     (zero? (get-in board [ny nx])))))
            piece)))

;; Rotate piece
(defn rotate-piece [piece]
  (mapv (fn [[x y]] [y (- x)]) piece))

;; Update game state
(defn update-state [state]
  (let [[x y] (:piece-position state)
        new-position [x (inc y)]
        new-state (assoc state :piece-position new-position)]
    (if (valid-position? (:board state) (:current-piece state) new-position)
      new-state
      (-> state
          (assoc :board (merge-board (:board state) (:current-piece state) [x y]))
          (assoc :current-piece (rand-nth (vals shapes)))
          (assoc :piece-position [4 0])
          (assoc :score (+ (:score state) 10))))))

;; Merge piece into board
(defn merge-board [board piece position]
  (let [[x y] position]
    (reduce (fn [b [dx dy]]
              (let [nx (+ x dx)
                    ny (+ y dy)]
                (assoc-in b [ny nx] 1)))
            board
            piece)))

;; Render board
(defn render [state]
  (doseq [row (:board state)]
    (println (clojure.string/join "" (map (fn [cell] (if (zero? cell) "." "X")) row)))
  (println "Score:" (:score state)))

;; Main loop
(defn -main []
  (let [state (init-game)]
    (loop [s state]
      (render s)
      (Thread/sleep 500)
      (recur (update-state s)))))
