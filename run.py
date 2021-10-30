from src.main import main

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("您停止了音乐播放！")
