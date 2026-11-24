import sys
import speedtest 

def the_speedtest():
    test = speedtest.Speedtest()

    print("Finding the best server...")
    test.get_best_server()

    print("Testing download speed...")

    download = test.download()
    
    download_mbps = download / 1_000_000

    print(f"Download Speed: {download_mbps:.2f} Mbps")

def main():
    the_speedtest()

main()

