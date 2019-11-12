package com.weljak.feeddashboard.controllers;

import com.weljak.feeddashboard.service.DbEntriesService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
@RequiredArgsConstructor
public class EntriesController {
    final private DbEntriesService dbEntriesService;

    @GetMapping("/entries")
    public String getEntriesPage(Model md) {
        md.addAttribute("entry", dbEntriesService.listAllEntries());
        return "entry";
    }
}
