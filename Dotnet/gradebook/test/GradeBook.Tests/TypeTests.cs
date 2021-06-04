using System;
using Xunit;

namespace GradeBook.Tests
{
    public delegate string WriteLogDelegate(string logMessage);

    public class TypeTests
    {
        int count = 0;

        [Fact]
        public void WriteLogDelegateCanPointToMethod()
        {
            WriteLogDelegate log = ReturnMessage;

            log += ReturnMessage;
            log += IncrementCount;

            var result = log("Hello!");
            Assert.Equal(3, count);
        }

        string IncrementCount(string message)
        {
            count++;
            return message.ToLower();
        }
        string ReturnMessage(string message)
        {
            count++;
            return message;
        }


        [Fact]
        public void StringsBehaveLiekValueTypes()
        {
            //arrange
            string name = "Carol";
            var upper = MakeUppercase(name);

            //assert
            Assert.Equal("Carol", name);
            Assert.Equal("CAROL", upper);
        }

        [Fact]
        public void ValueTypeAlsoPassedByValue()
        {
            //arrange
            var x = GetInt();
            SetInt(ref x);

            //assert
            Assert.Equal(42, x);
        }

        [Fact]
        public void CSharpIsPassedByRef()
        {
            //arrange
            var book1 = GetBook("Book 1");
            GetBookSetName2(out book1, "New Name");

            //assert
            Assert.Equal("New Name", book1.Name);
        }

        [Fact]
        public void CSharpIsPassedByValue()
        {
            //arrange
            var book1 = GetBook("Book 1");
            GetBookSetName(book1, "New Name");

            //assert
            Assert.Equal("Book 1", book1.Name);
        }

        [Fact]
        public void CanSetNameFromReference()
        {
            //arrange
            var book1 = GetBook("Book 1");
            SetName(book1, "New Name");

            //assert
            Assert.Equal("New Name", book1.Name);
        }

        [Fact]
        public void GetBookReturnsDifferentObjects()
        {
            //arrange
            var book1 = GetBook("Book 1");
            var book2 = GetBook("Book 2");

            //assert
            Assert.Equal("Book 1", book1.Name);
            Assert.Equal("Book 2", book2.Name);
            Assert.NotSame(book1, book2);
        }

        [Fact]
        public void TwoVarsCanReferenceSameObject()
        {
            //arrange
            var book1 = GetBook("Book 1");
            var book2 = book1;

            //assert
            Assert.Same(book1, book2);
            Assert.True(Object.ReferenceEquals(book1, book2));

        }

        //act
        private string MakeUppercase(string parameter)
        {
            return parameter.ToUpper();
        }
        private void SetInt(ref int y)
        {
            y = 42;
        }
        private int GetInt()
        {
            return 3;
        }
        private void GetBookSetName2(out Book book, string name)
        {
            book = new Book(name);
        }

        private void GetBookSetName(Book book, string name)
        {
            book = new Book(name);
            book.Name = name;
        }

        Book GetBook(string name)
        {
            return new Book(name);
        }

        private void SetName(Book book, string name)
        {
            book.Name = name;
        }


    }
}
