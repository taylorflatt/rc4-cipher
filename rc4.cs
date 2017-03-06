using System;
using System.Collections.Generic;

static class RC4
{
    static void Main(string[] args)
    {
        // Operating on a 3-bit key as an example.
        var k = new int[] { 2, 6, 1, 5 };
        var text = new int[] { 1, 3, 1, 2 };

        var s = new List<int>() { 0, 1, 2, 3, 4, 5, 6, 7 };
        var t = new List<int>() { 2, 6, 1, 5, 2, 6, 1, 5 };

        KSA(s, t);
        var temp = PRGA(s, text);

        Console.Write("Cipher = [");
        foreach (var element in temp)
        {
            Console.Write(element + " ");
        }
        Console.WriteLine("]");
    }

    public static List<int> PRGA(List<int> s_list, int[] text)
    {
        int i = 0, j = 0;
        var cipher = new List<int>();
        for(int index = 0; index < text.Length; index++)
        {
            i = (i + 1) % 8;
            j = (j + s_list[i]) % 8;
            s_list.Swap(i, j);
            var t = (s_list[i] + s_list[j]) % 8;
            var k = s_list[t];
            cipher.Add(k ^ text[index]);
        }

        return cipher;
    }

    public static void KSA(List<int> s_list, List<int> t_list)
    {
        var j = 0;
        for (int i = 0; i < 8; i++)
        {
            j = (j + s_list[i] + t_list[i]) % 8;
            s_list.Swap(i, j);
        }
    }

    public static void Swap(this List<int> list, int i, int j)
    {
        var temp = list[i];
        list[i] = list[j];
        list[j] = temp;
    }
}
