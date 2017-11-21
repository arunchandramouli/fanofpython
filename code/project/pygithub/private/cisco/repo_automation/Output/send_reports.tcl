proc send_email {recipient_list subject body {cc_list ""}}  {
global env
set msg "From: $env(USER)"
append msg \n "To: " [join $recipient_list ,]
append msg \n "Cc: " [join $cc_list ,]
append msg \n "Subject: $subject"
append msg \n "MIME-Version:1.0"
append msg \n "Content-Type :text/html"
append msg \n\n $body
exec /usr/lib/sendmail -oi -t << $msg
#mail -oi -t << $msg
}
set fid [open "Automation_GIT_PR.htm"]
set out [read $fid]
close $fid
send_email "arunkuch@cisco.com" "Bulldozer Automation - PR Report " $out
