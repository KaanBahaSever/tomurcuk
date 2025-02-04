import yt_dlp


def list_and_select_format(url):
    """Lists available formats and lets the user select one to download."""
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        formats = info.get("formats", [])

        # Display available formats
        print("\nAvailable Formats:")
        for f in formats:
            print(f"{f['format_id']:>5} | {f.get('ext', 'N/A'):<4} | {f.get('height', 'N/A')}p | {f.get('fps', 'N/A')} fps | {f.get('vcodec', 'N/A')} | {f.get('acodec', 'N/A')}")

        # User selects a format
        format_id = input("\nEnter the format ID to download: ").strip()

        # Download the selected format
        download_opts = {
            "format": format_id + "+bestaudio",  # Download selected video and best audio
            "outtmpl": "%(title)s.%(ext)s",  # Save as title.ext
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }]
        }
        with yt_dlp.YoutubeDL(download_opts) as ydl:
            ydl.download([url])


video_url = "https://www.youtube.com/watch?v=wjQx_dGUke0&ab_channel=QveenHerby"
list_and_select_format(video_url)
