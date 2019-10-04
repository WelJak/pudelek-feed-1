package com.weljak.storageservice.webapi;

import com.weljak.storageservice.checker.CheckerService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
public class CheckerController {
    private final CheckerService checkerService;

    @PostMapping("/check")
    public ResponseEntity<CheckerResponse> checkMessage(@RequestBody CheckerRequest checkerRequest) {
        return new ResponseEntity(checkerService.checkIfMessageWasSent(checkerRequest), HttpStatus.OK);
    }

    @PostMapping("/add")
    public ResponseEntity<CheckerResponse> sendMessage(@RequestBody CheckerRequest checkerRequest) {
        return new ResponseEntity(checkerService.sendMessage(checkerRequest), HttpStatus.OK);
    }
}