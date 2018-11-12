﻿# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("艾琳")


# 游戏在此开始。

label start:
    
    if renpy.can_load( 'save_1' ):
        $renpy.load( 'save_1' )
    else:
        $renpy.save( 'save_1' )

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为“bg room.png”或“bg room.jpg”）来显示。

    scene bg room

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # “eileen happy.png”的文件来将其替换掉。

    show eileen happy

    # 此处显示各行对话。

    e "您已创建一个新的 Ren'Py 游戏。"
    
    $renpy.save( 'save_1' )
    
    e '233333333333333333333333333333333333333333333333333.'

    # 此处为游戏结尾。

    return
