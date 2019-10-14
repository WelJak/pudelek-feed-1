package com.weljak.storageservice.webapi;

import com.weljak.storageservice.checker.CheckerService;
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
public class CheckerController {
    private final CheckerService checkerService;

    @PostMapping("/check")
    public ResponseEntity<CheckerResponse> checkMessage(@RequestBody CheckerRequest checkerRequest) {
        boolean wasSent = checkerService.checkIfMessageWasSent(checkerRequest);
        CheckerResponse response = new CheckerResponse(wasSent);
        if (wasSent) {
            String message = String.format("message %s has been already sent", checkerRequest.getEntryid());
            log.info(message);
        }else{
            String message = String.format("message %s has not been sent yet", checkerRequest.getEntryid());
            log.info(message);
        }
        return new ResponseEntity<>(response, HttpStatus.OK);
    }


}