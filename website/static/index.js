function deleteTicket(ticketId){
    fetch('/delete-ticket', {
        method: 'POST',
        body: JSON.stringify({ ticketId: ticketId, titleId: titleId })
    }).then((_res) => {
        window.location.href= "/";
    });
}
