package com.jrp.pma.dao;

import com.jrp.pma.dto.EmployeeProject;
import com.jrp.pma.entities.Employee;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

public interface EmployeeRepository extends CrudRepository<Employee,Long> {

    @Override
    public List<Employee> findAll();

    @Query(nativeQuery = true, value = "SELECT emp.first_name as firstName, emp.last_name as lastName, " +
            "COUNT(proj_emp.employeeID) as projectCount FROM employee emp LEFT JOIN " +
            "project_employee proj_emp ON proj_emp.employeeID = emp.employeeID GROUP BY emp.first_name, " +
            "emp.last_name ORDER BY 3 DESC")
    public List<EmployeeProject> employeeProjects();
}
