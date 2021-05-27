package com.jrp.pma.controllers;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.jrp.pma.dao.EmployeeRepository;
import com.jrp.pma.dao.ProjectRepository;
import com.jrp.pma.dto.ChartData;
import com.jrp.pma.dto.EmployeeProject;
import com.jrp.pma.entities.Project;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Controller
public class HomeController {

    @Autowired
    ProjectRepository projectRepository;

    @Autowired
    EmployeeRepository employeeRepository;

    @GetMapping("/")
    public String displayHome(Model model) throws JsonProcessingException {

        Map<String, Object> map = new HashMap<>();

        // we are querying the database for projects
        List<Project> projects = projectRepository.findAll();
        model.addAttribute("projectsList",projects);

        // we are querying the database for project status
        List<ChartData> projectStatus = projectRepository.getProjectStatus();

        // Let's convert projectData object into a json structure for use in javascript
        ObjectMapper objectMapper = new ObjectMapper();
        String jsonString =objectMapper.writeValueAsString(projectStatus);
        // This jsonString will look like this (3 arrays, in this case):
        // {["NOTSTARTED", 1], ["INPROGRESS",2], ["COMPLETED",1]}

        model.addAttribute("projectStatusCount", jsonString);

        // we are querying the database for employees
        List<EmployeeProject> employeesProjectCount = employeeRepository.employeeProjects();
        model.addAttribute("employeesListProjectCount",employeesProjectCount);

        return "main/home";
    }
}
