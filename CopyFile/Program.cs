// See https://aka.ms/new-console-template for more information

// 从命令行参数中获取源目录和目标目录，如果没有提供则使用默认值
string source = args.Length > 0 ? args[0] : @"C:\Users\user\source";
string target = args.Length > 1 ? args[1] : @"C:\Users\user\target";
// 遍历源目录下的所有文件，包括子目录中的文件
foreach (string file in Directory.GetFiles(source, "*", SearchOption.AllDirectories))
{
    // 获取文件大小，单位为字节
    long size = new FileInfo(file).Length;
    // 判断文件大小是否在指定范围内，并重命名文件
    if (size > 5120 && size < 94800)
    {
        File.Copy(file, Path.Combine(target, "profile.sav"), true);
    }
    else if (size > 97200)
    {
        File.Copy(file, Path.Combine(target, "save_0.sav"), true);
    }
}
Console.WriteLine("Success!");
Console.ReadKey();