using System;

namespace GradeBook
{

    public class Statistics
    {
        public double HighValue;
        public double LowValue;
        public double Sum;
        public int Count;

        public double Average
        {
            get
            {
                return Sum / Count;
            }
        }

        public char Letter
        {
            get
            {
                switch (Average)
                {

                    case var d when d >= 90.0:
                        return 'A';

                    case var d when d >= 80.0:
                        return 'B';

                    case var d when d >= 70.0:
                        return 'C';

                    case var d when d >= 60.0:
                        return 'D';

                    default:
                        return 'F';
                }
            }

        }
        public void Add(double number)
        {
            Sum += number;
            Count += 1;
            LowValue = Math.Min(number, LowValue);
            HighValue = Math.Max(number, HighValue);
        }
        public Statistics()
        {

            Count = 0;
            Sum = 0.0;
            HighValue = double.MinValue;
            LowValue = double.MaxValue;
        }
    }
}