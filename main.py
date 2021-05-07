import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        self.master.geometry("300x200")

        # Window内にFrameを作成する。
        # 親要素をWindowとする。
        # width : Frameの幅を設定する。
        # height : Frameの高さを設定する。
        # bg : 背景色を設定する。
        # 色の設定を変更する場合 : http://www.tcl.tk/man/tcl/TkCmd/colors.htm
        frame = tk.Frame(self.master, width=400, height=400,
                         bg="green")

        # ラベルWidgetを作成する。
        # text : テキスト情報
        # width : 幅の設定
        # height : 高さの設定
        # bg : 背景色の設定
        # 色の設定を変更する場合 : http://www.tcl.tk/man/tcl/TkCmd/colors.htm
        # relief : 枠の設定
        # reliefについて : https://cercopes-z.com/Python/stdlib-tkinter-widget-frame-py.html#detail-relief
        label = tk.Label(frame, text="1", width=30, height=15,
                         bg="orchid4", relief="raised")

        # packを利用して、Frameの配置を行う。
        frame.pack()

        # Frameを親要素とした場合に、ラベルWidgetをどのように配置するのか?
        label.place(x=40, y=40)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    app.mainloop()
