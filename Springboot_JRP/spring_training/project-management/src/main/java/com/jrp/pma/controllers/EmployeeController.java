package com.jrp.pma.controllers;

import com.jrp.pma.dao.EmployeeRepository;
import com.jrp.pma.entities.Employee;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/employees")
public class EmployeeController {

    @Autowired
    EmployeeRepository employeeRepository;

    @GetMapping("/new")
    public String displayEmployeeForm(Model model){

        Employee aEmployee = new Employee();

        model.addAttribute("employee", aEmployee);
        return "new_employee";
    }

    @PostMapping("/save")
    public String createEmployee(Employee employee, Model model){

        //This should handle the saving to the database
        employeeRepository.save(employee);

        //use the redirect to prevent duplicate submissions
        return "redirect:/employees/new";
    }
}
