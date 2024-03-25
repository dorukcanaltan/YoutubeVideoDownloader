from pytube import YouTube

# İlerleme durumunu gösteren fonksiyon
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f'İndirme Durumu: %{percentage_of_completion:.2f} tamamlandı.')

# İndirme tamamlandığında çağrılacak fonksiyon
def on_complete(stream, file_path):
    print(f'İndirme tamamlandı. Dosya yolu: {file_path}')

def download_video(url, path=''):
    yt = YouTube(url)
    yt.register_on_progress_callback(on_progress)
    yt.register_on_complete_callback(on_complete)

    # Yüksek çözünürlüklü stream'i seçip indiriyoruz.
    yt.streams.get_highest_resolution().download(output_path=path)

url = input("Enter the URL: ")
download_video(url)
