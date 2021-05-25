package com.jrp.pma.controllers;

import com.jrp.pma.dao.ProjectRepository;
import com.jrp.pma.entities.Project;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/projects")
public class ProjectController {

    @Autowired
    ProjectRepository projectRepository;

    @GetMapping("/new")
    public String displayProjectForm(Model model){

        Project aProject = new Project();

        model.addAttribute("project", aProject);
        return "new_project";
    }

    @PostMapping("/save")
    public String createProject(Project project, Model model){

        //This should handle the saving to the database
        projectRepository.save(project);

        //use the redirect to prevent duplicate submissions
        return "redirect:/projects/new";
    }
}
