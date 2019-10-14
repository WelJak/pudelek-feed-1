package com.weljak.storageservice.webapi;

import com.weljak.storageservice.messages.MessageMarkService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@Slf4j
@RestController
@RequiredArgsConstructor
public class MessageMarkController {
    private final MessageMarkService messageMarkService;

    @GetMapping("/messages/{entryid}/mark")
    public ResponseEntity<MessageMarkResponse> markMessage(@PathVariable String entryid) {
        boolean response = messageMarkService.markMessage(entryid);
        if (response) {
            String message = String.format("message %s has been successfully marked", entryid);
            log.info(message);
        } else {
            String message = String.format("an error occurred during marking message %s", entryid);
            log.info(message);
        }
        MessageMarkResponse messageMarkResponse = new MessageMarkResponse(response);
        return new ResponseEntity<>(messageMarkResponse, HttpStatus.OK);
    }
}
