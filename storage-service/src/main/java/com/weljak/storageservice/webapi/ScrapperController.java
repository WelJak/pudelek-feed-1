package com.weljak.storageservice.webapi;

import com.weljak.storageservice.scrapper.ScrapperService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@Slf4j
@RestController
@RequiredArgsConstructor
public class ScrapperController {
    private final ScrapperService scrapperService;

    @PostMapping("/scrapnews")
    public ResponseEntity<ScrapperResponse> scrapNews(@RequestBody String url){
        ScrapperResponse scrapperResponse = scrapperService.fetchEntryDetails(url);
        return new ResponseEntity<>(scrapperResponse, HttpStatus.OK);
    }
}
