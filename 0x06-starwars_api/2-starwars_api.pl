#!/usr/bin/perl
use strict;
use warnings;
use LWP::UserAgent;
use JSON;

sub fetch {
    my $url = shift;
    my $ua = LWP::UserAgent->new;
    my $response = $ua->get($url);
    if ($response->is_success) {
        return decode_json($response->decoded_content);
    } else {
        print "Request failed. Status code: ", $response->status_line, "\n";
        return;
    }
}

sub fetch_characters_recursively {
    my ($char_data, $index) = @_;
    if ($index >= scalar @$char_data) {
        return;
    }
    my $character_url = $char_data->[$index];
    my $character = fetch($character_url);
    if (defined $character) {
        print $character->{name}, "\n";
    }
    fetch_characters_recursively($char_data, $index + 1);
}

sub fetch_movie_characters {
    my $movie_id = shift;
    my $api_url = "https://swapi-api.alx-tools.com/api/films/$movie_id/";
    my $movie_data = fetch($api_url);
    if (defined $movie_data) {
        fetch_characters_recursively($movie_data->{characters}, 0);
    }
}

my $movie_id = $ARGV[0];
fetch_movie_characters($movie_id);
