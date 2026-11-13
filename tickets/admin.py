from django.contrib import admin

from tickets.models import Category, Ticket, Comment

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name', 
        'description',
        'created_at',
    )

    search_fields = ('name',)

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'created_by',
        'assigned_to',
        'status',
        'priority',
        'created_at',
    )

    list_filter = (
        'category',
        'status',
        'priority',
        'created_at',
    )

    search_fields = (
        'title',
        'description',
        'created_by__username',
        )

    readonly_fields = (
        'created_at',
        'updated_at',
    )

    inlines = [CommentInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'ticket',
        'author',
        'created_at',
    )

    search_fields = (
        'message',
        'author__username',
        'ticket_title',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )