 select concat('la superficie de La Plateforme est de ', sum(superficie), 'm2')
    -> as message
    -> from etage;
