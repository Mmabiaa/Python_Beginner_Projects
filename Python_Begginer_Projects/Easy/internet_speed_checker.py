import speedtest

def speed_check():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    ping = st.results.ping

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")

if __name__ == "__main__":
    try:
        speed_check()
    except speedtest.ConfigRetrievalError as e:
        print(f"Error: Unable to retrieve configuration. {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
