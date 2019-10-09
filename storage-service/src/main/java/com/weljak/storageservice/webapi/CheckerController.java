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
        boolean wasSent = checkerService.checkIfMessageWasSent(checkerRequest);
        CheckerResponse response = new CheckerResponse(wasSent);
        if (wasSent) {
            System.out.println("Wysłano");
        }
        return new ResponseEntity<>(response, HttpStatus.OK);
    }


}