package com.weljak.storageservice.message;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;
import java.util.List;

@Entity
@Getter
@Setter
@NoArgsConstructor
public class News {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "uuid", unique = true, nullable = false, updatable = false)
    private String uuid;

    @Column(name = "type", nullable = false)
    private String type;

    @Column(name = "entry_id", unique = true, nullable = false)
    private String entry_id;

    @Column(name = "post_date", nullable = false)
    private String post_date;

    @Column(name = "title", nullable = false)
    private String title;

    @Column(name = "description", nullable = false)
    private String description;

    @OneToMany(mappedBy = "tags")
    private List<Tags> tags;

    @Column(name ="link", nullable = false)
    private String link;
}
