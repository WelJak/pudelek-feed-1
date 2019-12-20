package com.weljak.feeddashboard.controllers;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
@RequiredArgsConstructor
public class AdminController {
    @GetMapping("/pudelek/admin/panel/login")
    public String getAdminLoginPanel(Model model, String error, String logout){
        if(error !=null)
            model.addAttribute("error", "Incorrect login and/or password");
        if(logout!=null)
            model.addAttribute("message", "You have been logged out");
        return "adminlogin";
    }
    @GetMapping("/pudelek/admin/panel/costam")
    public String getAdminPostLoginPanel(){
        return "postlogin";
    }
}
