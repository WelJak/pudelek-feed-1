package com.weljak.storageservice.webapi;

import com.weljak.storageservice.messages.MessageDetailService;
import com.weljak.storageservice.news.News;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
public class MessageDetailsController {
    private final MessageDetailService messageDetailService;

    @GetMapping("/messages/{entryid}")
    public ResponseEntity<MessageDetailResponse> getMessage(@PathVariable String entryid, Model model) {
        final News entry = messageDetailService.getMessage(entryid);
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

}
