import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")

        # Window内にFrameを作成する。
        # 親要素をWindowとする。
        # width : Frameの幅を設定する。
        # height : Frameの高さを設定する。
        # bg : 背景色を設定する。
        # 色の設定を変更する場合 : http://www.tcl.tk/man/tcl/TkCmd/colors.htm
        # borderwidth : 境界線の幅を指定する。
        # relief : 境界線のデザインを設定する。
        # reliefについて : https://cercopes-z.com/Python/stdlib-tkinter-widget-frame-py.html#detail-relief
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master, width=400, height=400, borderwidth=20,
                         bg="green", relief=tk.SUNKEN)

        # ラベルWidgetを作成する。
        # text : テキスト情報
        # width : 幅の設定
        # height : 高さの設定
        # bg : 背景色の設定
        # 色の設定を変更する場合 : http://www.tcl.tk/man/tcl/TkCmd/colors.htm
        # relief : 境界線の設定
        # reliefについて : https://cercopes-z.com/Python/stdlib-tkinter-widget-frame-py.html#detail-relief
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label = tk.Label(frame, text="1", width=30, height=15,
                         bg="orchid4", relief="raised")

        # packを利用して、Frameの配置を行う。
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # Frameを親要素とした場合に、ラベルWidgetをどのように配置するのか?
        label.place(x=40, y=40)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
