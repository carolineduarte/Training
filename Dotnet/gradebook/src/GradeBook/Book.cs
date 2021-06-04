using System;
using System.Collections.Generic;
using System.IO;

namespace GradeBook
{
    public delegate void GradeAddedDelegate(object sender, EventArgs args);

    public class NameObject
    {
        public NameObject(string name)
        {
            Name = name;
        }

        public string Name
        {
            get; set;
        }
    }
    public interface IBook
    {
        void AddGrade(double grade);
        Statistics GetStatistics();
        string Name { get; }
        event GradeAddedDelegate GradeAdded;
    }
    public abstract class Book : NameObject, IBook
    {
        public Book(string name) : base(name)
        {
        }

        public abstract event GradeAddedDelegate GradeAdded;

        public abstract void AddGrade(double grade);

        public abstract Statistics GetStatistics();

    }
    public class DiskBook : Book
    {
        public DiskBook(string name) : base(name)
        {
        }

        public override event GradeAddedDelegate GradeAdded;

        public override void AddGrade(double grade)
        {
            var writer = File.AppendText($"{Name}.txt");
            writer.WriteLine(grade);
        }

        public override Statistics GetStatistics()
        {
            throw new NotImplementedException();
        }
    }
    public class InMemoryBook : Book
    {
        private List<double> grades;
        //private string name;

        public const string CATEGORY = "Science";

        public override event GradeAddedDelegate GradeAdded;

        public InMemoryBook(string name) : base(name)
        {
            this.grades = new List<double>();
            this.Name = name;
        }
        public override void AddGrade(double grade)
        {
            if (grade <= 100 && grade >= 0)
            {
                grades.Add(grade);
                if (GradeAdded != null)
                {
                    GradeAdded(this, new EventArgs());
                }
            }
            else
            {
                throw new ArgumentException($"Invalid {nameof(grade)}!");
            }
        }

        public void AddLetterGrade(char letter)
        {

            switch (letter)
            {
                case 'A':
                    AddGrade(90);
                    break;
                case 'B':
                    AddGrade(80);
                    break;
                case 'C':
                    AddGrade(70);
                    break;
                default:
                    AddGrade(0);
                    break;
            }
        }

        public override Statistics GetStatistics()
        {
            var result = new Statistics();
            result.Average = 0.0;
            result.LowValue = double.MaxValue;
            result.HighValue = double.MinValue;

            for (var index = 0; index < grades.Count; index++)
            {
                result.LowValue = Math.Min(grades[index], result.LowValue);
                result.HighValue = Math.Max(grades[index], result.HighValue);
                result.Average += grades[index];
            };

            result.Average = result.Average / grades.Count;

            switch (result.Average)
            {

                case var d when d >= 90.0:
                    result.Letter = 'A';
                    break;

                case var d when d >= 80.0:
                    result.Letter = 'B';
                    break;

                case var d when d >= 70.0:
                    result.Letter = 'C';
                    break;

                case var d when d >= 60.0:
                    result.Letter = 'D';
                    break;

                default:
                    result.Letter = 'F';
                    break;

            }

            return result;
        }
    }
}