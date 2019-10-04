package com.weljak.storageservice.webapi;

import com.weljak.storageservice.checker.CheckerService;
import com.weljak.storageservice.message.News;
import com.weljak.storageservice.message.newsrepo.NewsRepo;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequiredArgsConstructor
public class CheckerController {
    private final CheckerService checkerService;

    @PostMapping("/check")
    public ResponseEntity<CheckerResponse> checkMessage(@RequestBody CheckerRequest checkerRequest) {
        return new ResponseEntity(checkerService.checkIfMessageWasSent(checkerRequest), HttpStatus.OK);
    }
    /*@PostMapping("/add")  // NIE DZIAŁA
    public ResponseEntity<CheckerResponse> sendMessage(@RequestBody CheckerRequest checkerRequest) {
        return new ResponseEntity(News.save(checkerRequest), HttpStatus.OK);
    }*/
}