using System;
using System.IO;
using System.Linq;

namespace ConsoleApp
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var directory = Directory.GetFiles("../../../");
            var filePath = directory.FirstOrDefault(item => item.Contains("input"));
            if (filePath == null) throw new NullReferenceException("Couldn't find input.txt");
            var binaryData = File.ReadAllLines(filePath);

            var program = new Program();
            Console.WriteLine(program.RunDiagnostics(binaryData));
        }

        private (int, int) RunDiagnostics(string[] binaryData)
        {
            var gamma = FindBasicValue(binaryData);
            var epsilon = FindBasicValue(binaryData, false);

            var oxygenRating = FindRating(binaryData);
            var co2Rating = FindRating(binaryData, searchCommon: false);

            return (Convert.ToInt32(gamma, 2) * Convert.ToInt32(epsilon, 2),
                Convert.ToInt32(oxygenRating, 2) * Convert.ToInt32(co2Rating, 2));
        }

        private string FindRating(string[] binaryData, int binaryIndex = 0, bool searchCommon = true)
        {
            if (binaryData.Length == 1) return binaryData[0];

            var zerosCount = 0;
            var onesCount = 0;
            for (int i = 0; i < binaryData.Length; i++)
            {
                if (binaryData[i][binaryIndex] == '1')
                {
                    onesCount++;
                }
                else
                {
                    zerosCount++;
                }
            }

            char digit;
            int newSize;
            if (searchCommon)
            {
                digit = Math.Max(zerosCount, onesCount) == onesCount ? '1' : '0';
                newSize = digit == '1' ? onesCount : zerosCount;
            }
            else
            {
                digit = Math.Min(zerosCount, onesCount) == zerosCount ? '0' : '1';
                newSize = digit == '0' ? zerosCount : onesCount;
            }
            
            var newBinaryData = RemoveRows(binaryData, digit, newSize, binaryIndex);
            return FindRating(newBinaryData, ++binaryIndex, searchCommon);
        }

        private string[] RemoveRows(string[] data, char digit, int size, int binaryIndex)
        {
            string[] filteredData = new string[size];
            int filteredIndex = 0;

            for (int i = 0; i < data.Length; i++)
            {
                if (data[i][binaryIndex] == digit)
                {
                    filteredData[filteredIndex++] = data[i];
                }
            }

            return filteredData;
        }

        private string FindBasicValue(string[] binaryData, bool searchCommon = true)
        {
            var value = "";
            var binaryValueLength = binaryData[0].Length;
            for (int binaryIndex = 0; binaryIndex < binaryValueLength; binaryIndex++)
            {
                var zerosCount = 0;
                var onesCount = 0;
                for (int i = 0; i < binaryData.Length; i++)
                {
                    if (binaryData[i][binaryIndex] == '1')
                    {
                        onesCount++;
                    }
                    else
                    {
                        zerosCount++;
                    }
                }

                string digit;
                if (searchCommon)
                {
                    digit = Math.Max(zerosCount, onesCount) == zerosCount ? "0" : "1";
                }
                else
                {
                    digit = Math.Min(zerosCount, onesCount) == zerosCount ? "0" : "1";
                }

                value += digit;
            }

            return value;
        }
    }
}