package com.weljak.storageservice.webapi;

import com.weljak.storageservice.messages.MessagesService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequiredArgsConstructor
public class MessagesController {
    private final MessagesService messagesService;

    @GetMapping("/messages")
    public ResponseEntity<MessagesResponse> getMessages() {
        List<String> response_array = messagesService.getMessages();
        MessagesResponse response = new MessagesResponse(response_array);
        return new ResponseEntity<>(response, HttpStatus.OK);
    }
}
