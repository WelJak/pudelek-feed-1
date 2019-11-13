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

    @GetMapping("/messagesId")
    public ResponseEntity<MessagesResponse> getMessages() {
        List<String> response_array = messagesService.getMessagesIdList();
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
        MessageMarkResponse messageMarkResponse = new MessageMarkResponse(response);
        return new ResponseEntity<>(messageMarkResponse, HttpStatus.OK);
    }

    @GetMapping("/messages/all")
    public ResponseEntity<AllMessagesResponse> getAllMessages(){
        List<News> responseArray = messagesService.listAllMessages();
        AllMessagesResponse response = new AllMessagesResponse(responseArray);
        return new ResponseEntity<>(response, HttpStatus.OK);
    }

}
