
init python:
    # FTP操作
    import ftplib

    host = '212.64.16.39'
    username = 'ftp212_64_16_39'
    password = 'YuudachiXMMY0914'
    file = '1.txt'

    try:
        f = ftplib.FTP(host)  # 实例化FTP对象
    except BaseException:
        pass
    else:
        try:
            f.login(username, password)  # 登录
        except BaseException:
            pass
        else:
            # 获取当前路径
            f.cwd('cdkey')
            pwd_path = f.pwd()

    #print("FTP当前路径:", pwd_path)

    # 逐行读取ftp文本文件
    # f.retrlines('RETR %s' % file)

    def find_key(key):
        try:
            key_list = f.nlst()
        except BaseException:
            return False
        else:
            for cdkey in key_list:
                if key==cdkey:
                    return True
            return False

    def ftp_download(a):
        if find_key(a):
            file_remote = str(a)+'.txt'
            file_local = 'C:\\GamePython\\YiNv2\\game\\download\\'+str(a)+'.txt'
            bufsize = 1024  # 设置缓冲器大小
            try:
                fp = open(file_local, 'wb')
            except BaseException:
                pass
            else:
                try:
                    f.retrbinary('RETR %s' % file_remote, fp.write, bufsize)
                except BaseException:
                    pass
                else:
                    fp.close()


    def ftp_upload():
        file_remote = 'ftp_upload.txt'
        file_local = 'C:\\GamePython\\YiNv2\\game\\download\\up_download.txt'
        bufsize = 1024  # 设置缓冲器大小
        fp = open(file_local, 'rb')
        f.storbinary('STOR ' + file_remote, fp, bufsize)
        fp.close()
        f.quit()


    #f.quit()

screen ftp_log():
    tag menu

    frame:
        add bg.random

    button:
        pos( 140 , 390 )
        idle_background "gui/nav/block.png"
        hover_background "gui/nav/block.png"
        action Function(ftp_download,'qwerasdf')
    
    add "gui/nav/return.png" pos( 220 , 440 )