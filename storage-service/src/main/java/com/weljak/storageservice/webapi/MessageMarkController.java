package com.weljak.storageservice.webapi;

import com.weljak.storageservice.messages.MessageMarkService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
public class MessageMarkController {
    private final MessageMarkService messageMarkService;

    @GetMapping("/messages/{entryid}/mark")
    public ResponseEntity<MessageMarkResponse> markMessage(@PathVariable String entryid){
         boolean response = messageMarkService.markMessage(entryid);
         MessageMarkResponse messageMarkResponse = new MessageMarkResponse(response);
        return new ResponseEntity<>(messageMarkResponse, HttpStatus.OK);
    }
}
