package com.weljak.feeddashboard.controllers;

import com.weljak.feeddashboard.service.AppacheHttpEntriesRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
@RequiredArgsConstructor
public class HomeController {

    private final AppacheHttpEntriesRepository dbEntriesService;

    @GetMapping("/")
    public String getHomePage() {
        return "home";
    }

}
