package com.weljak.feeddashboard.controllers;

import com.weljak.feeddashboard.service.DbEntriesService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
@RequiredArgsConstructor
public class HomeController {

    private final DbEntriesService dbEntriesService;

    @GetMapping("/")
    public String getHomePage() {
        return "home";
    }

}
