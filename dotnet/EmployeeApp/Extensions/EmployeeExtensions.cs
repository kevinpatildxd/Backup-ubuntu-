using EmployeeApp.Models;

namespace EmployeeApp.Extensions
{
    public static class EmployeeExtensions
    {
        public static string GetFullName(this Employee employee)
        {
            return $"{employee.FirstName} {employee.LastName}";
        }
    }
}
