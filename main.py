
'''
#relionのmaskcreationに用いるディレクトリ(J30みたいな感じ)を選択すると
maskcreationにもちいるmrc file(sharp.mrc?)のpathを保存
そのhalf file2つも別のリストにpathを保存する
relionの解析ディレクトリのパスを選択する
2つのhalf fileを選択されたrelionの解析ディレクトリにcopyする
２つのcopyされたhalf fileの名前をrenameする
'''
import Copy2Relion
import ReadFile

readfile = ReadFile.ReadFile()
copy2relion = Copy2Relion.Copy2Relion()

half_map = readfile.reedfile()
copy2relion.copy2relion(half_map)


print("プログラムを終了しています")