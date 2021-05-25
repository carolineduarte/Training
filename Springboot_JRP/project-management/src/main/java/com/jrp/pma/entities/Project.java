package com.jrp.pma.entities;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Getter
@Setter
@NoArgsConstructor
@Entity
public class Project {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private long projectID;
    private String name;
    private String stage; //NOTSTARTED, COMPLETED, INPROGRESS
    private String description;

    public Project(String name, String stage, String description) {
        this.name = name;
        this.stage = stage;
        this.description = description;
    }
}
