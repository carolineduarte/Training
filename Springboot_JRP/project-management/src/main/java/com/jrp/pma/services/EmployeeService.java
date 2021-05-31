package com.jrp.pma.services;

import com.jrp.pma.dao.EmployeeRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class EmployeeService {

    // Field injection:
    @Autowired
    EmployeeRepository employeeRepository;

    // Constructor injection (without the @Autowired at the repo above.)
    public EmployeeService(EmployeeRepository employeeRepository){
        this.employeeRepository = employeeRepository;
    }

    // Setter injection (without the @Autowired at the repo above.)
    @Autowired
    public void setEmployeeRepository(EmployeeRepository employeeRepository){
        this.employeeRepository = employeeRepository;
    }

}
