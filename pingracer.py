import platform
import time
import subprocess

def ping_node(ip):
    os_type = platform.system()
    if os_type == "Windows":
        command = ["ping", "-n", "1", ip]
    else:
        command = ["ping", "-c", "1", ip]
    start_time = time.time()
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    end_time = time.time()
    return end_time - start_time

def main():
    teams = {
        "Tailscale": ["192.168.1.1", "10.0.0.1"],
        "Regular IPs": ["8.8.8.8", "8.8.4.4"]
    }

    results = {}

    for team, ips in teams.items():
        print(f"Team {team} is racing! {'🟢' if team == 'Tailscale' else '🏃'}")
        total_time = 0.0
        for ip in ips:
            time_taken = ping_node(ip)
            total_time += time_taken
            print(f"  Pinging {ip}... Took {time_taken:.2f} seconds")
        results[team] = total_time
        print(f"Team {team} completed all pings in {total_time:.2f} seconds.")

    # Determine and print the winner
    winner = min(results, key=results.get)
    print(f"🎉 {winner} wins! Total time: {results[winner]:.2f}s")

if __name__ == "__main__":
    main()
