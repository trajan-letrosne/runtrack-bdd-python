 select concat ('la capacité de toute les salles est de :',sum(capacite))
    -> as message
    -> from salle;
