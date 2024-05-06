def download_progress(total_size, chunk_size=1024, duration=1):
    downloaded = 0
    while downloaded < total_size:
        downloaded += chunk_size
        progress = min(downloaded, total_size) / total_size
        progress_bar_length = 30
        filled_length = int(progress_bar_length * progress)
        bar = '=' * filled_length + '-' * (progress_bar_length - filled_length)
        status = f"[{'=' * filled_length}{' ' * (progress_bar_length - filled_length)}] {progress * 100:.2f}%"
        sys.stdout.write(f"\rLoading: {status}")
        sys.stdout.flush()
        time.sleep(duration)

    sys.stdout.write('\n')
    print("Done")
    time.sleep(1)
    os.system('cls')
