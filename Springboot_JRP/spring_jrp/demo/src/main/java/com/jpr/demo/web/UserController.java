package com.jpr.demo.web;

import com.jpr.demo.domain.Product;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.Arrays;
import java.util.Date;
import java.util.List;

@RestController
@RequestMapping("/user")
public class UserController {

    @RequestMapping("{userID}")
    public String displayUser(@PathVariable int userID){
        return "User found: " + userID;
    }

    @RequestMapping("{userID}/invoices")
    public String displayUserInvoices(@PathVariable int userID, @RequestParam(value = "date", required = false) Date dateOrNull){
        return "Invoice found for user: " + userID + " on the date " + dateOrNull;
    }

    @RequestMapping("{userID}/items")
    public List<String> displayStringJson(){

        return Arrays.asList("Shoes","Laptop","Button");
    }

    @RequestMapping("{userID}/products_as_json")
    public List<Product> displayProductsJson(){

        return Arrays.asList(new Product(1,"Shoes",45.99),
                new Product(2,"Laptop",2235.69), new Product(3,"Button",1.99));
    }
}
