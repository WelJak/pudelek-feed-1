package com.weljak.storageservice.webapi;

import com.weljak.storageservice.messages.MessagesService;
import com.weljak.storageservice.news.News;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@Slf4j
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

    @GetMapping("/messages/{entryid}")
    public ResponseEntity<MessageDetailResponse> getMessage(@PathVariable String entryid, Model model) {
        final News entry = messagesService.getMessage(entryid);
        model.addAttribute("id", entry.getEntryid());
        MessageDetailResponse messageDetailResponse = new MessageDetailResponse(
                entry.getUuid(),
                entry.getType(),
                entry.getEntryid(),
                entry.getPost_date(),
                entry.getTitle(),
                entry.getDescription(),
                entry.getTag(),
                entry.getLink(),
                entry.isWassent()
        );
        return new ResponseEntity<>(messageDetailResponse, HttpStatus.OK);
    }

    @GetMapping("/messages/{entryid}/mark")
    public ResponseEntity<MessageMarkResponse> markMessage(@PathVariable String entryid) {
        boolean response = messagesService.markMessage(entryid);
        if (response) {
            log.info("message {} has been successfully  marked", entryid);
        } else {
            log.info("an error occurred during marking message {}", entryid);
        }
        MessageMarkResponse messageMarkResponse = new MessageMarkResponse(response);
        return new ResponseEntity<>(messageMarkResponse, HttpStatus.OK);
    }

}
