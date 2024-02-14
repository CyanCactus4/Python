using static System.Console;
using static System.Math;

namespace Name
{
    class Program
    {
        static void Main(string[] args)
        {
            WriteLine("Введите число:");
            int par = int.Parse(ReadLine());
            WriteLine($"Все простые от 2 до {par} включительно:");
            for (int i = 2; i <= par; i++)
            {
                bool Flag = true;
                for (int j = 2; j <= Floor(Sqrt(i)); j++)
                {
                    if (i % j == 0)
                    {
                        Flag = false;
                        break;
                    }
                }
                if (Flag)
                    WriteLine(i);
            }
        }
    }
}