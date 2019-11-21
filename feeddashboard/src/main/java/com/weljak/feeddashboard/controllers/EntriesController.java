package com.weljak.feeddashboard.controllers;

import com.weljak.feeddashboard.service.AppacheHttpEntriesRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@Controller
@RequiredArgsConstructor
public class EntriesController {
    private final AppacheHttpEntriesRepository appacheHttpEntriesRepository;

    @GetMapping("/entries")
    public String getEntriesPage(Model md) {
        md.addAttribute("entry", appacheHttpEntriesRepository.listAllEntries());
        return "entry";
    }
    @GetMapping("/entries/{entryid}")
    public String getEntryDetails(Model md, @PathVariable String entryid){
        md.addAttribute("entrydetails",appacheHttpEntriesRepository.getEntryDetails(entryid));
        return "entrydetails";
    }
}
