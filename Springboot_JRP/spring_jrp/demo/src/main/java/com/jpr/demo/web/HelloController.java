/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.jpr.demo.web;

import org.springframework.web.bind.annotation.*;

/**
 *
 * @author carol
 */
@RestController
@RequestMapping("/greeting")
public class HelloController {

    // method = RequestMethod.GET is the default
    @RequestMapping("/basics")
    public String sayHello(){
        return "<h1>Hello!</h1>";
    }

    @RequestMapping("/proper")
    public String sayProperHello(){
        return "<h1>Hello there, how are you?</h1>";
    }

    @RequestMapping("/user_entry")
    public String userForm(){
        return "<form action=\"/greeting/user_greeting\" method = \"POST\" >\n" +
                "            <label for=\"fname\">First name:</label><br>\n" +
                "            <input type=\"text\" id=\"fname\" name=\"fname\"><br>\n" +
                "            <label for=\"lname\">Last name:</label><br>\n" +
                "            <input type=\"text\" id=\"lname\" name=\"lname\"><br><br>\n" +
                "            <input type=\"submit\" value=\"Submit\">\n" +
                "        </form>";
    }

    @RequestMapping(value = "/user_greeting", method = RequestMethod.POST)
    public String printUserGreeting(@RequestParam String fname, @RequestParam String lname){
        return "Hello there, " + fname + " " + lname;
    }

    @RequestMapping("/orders/{id}")
    public String getOrder(@PathVariable String id){
        return "Order ID: " + id;
    }
}
