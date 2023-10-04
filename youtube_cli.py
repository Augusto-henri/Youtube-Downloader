from pytube import YouTube

def video_downloader(video_url):
    # passing the url to the YouTube object
    my_video = YouTube(video_url)
    # downloading the video in high resolution
    my_video.streams.get_highest_resolution().download()
    # return the video title
    return my_video.title

# access streams, title, thumbnail_url, channel_id
#especifica resolução
# YouTube(url).streams.filter(res="Your_Resolution").first().download()

if __name__ == '__main__':
    youTube_link = input("Digite o link para baixar o vídeo:")

    try:

        print("Baixando o vídeo. Aguarde...")

        video_title = video_downloader(youTube_link)

        print(f'"{video_title}" downloaded successfully!!')
    except:
        print("Falha ao baixar o vídeo!")

