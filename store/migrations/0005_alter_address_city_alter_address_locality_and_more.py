# Generated by Django 4.0 on 2021-12-17 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('store', '0004_auto_20210529_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=150, verbose_name='Huyện/Thành phố'),
        ),
        migrations.AlterField(
            model_name='address',
            name='locality',
            field=models.CharField(max_length=150, verbose_name='Địa chỉ cụ thể'),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=150, verbose_name='Tỉnh'),
        ),
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Tên người dùng'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='sản phẩm'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Số lượng'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Cập nhật'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='tên người dùng'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(blank=True, null=True, upload_to='category', verbose_name='Hình ảnh danh mục'),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, verbose_name='Miêu tả danh mục'),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(verbose_name='Có hoạt động?'),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_featured',
            field=models.BooleanField(verbose_name='Có đề xuất?'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=55, verbose_name='Slug danh mục'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Tên danh mục'),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Cập nhật'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.address', verbose_name='Địa chỉ'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Thời gian đặt'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='Sản phẩm'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Số lượng'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Đang xử lý'), ('Accepted', 'Đã xác nhận đơn'), ('Packed', 'Đã đóng gói'), ('On The Way', 'Đang vận chuyển'), ('Delivered', 'Đã giao hàng'), ('Cancelled', 'Đã huỷ')], default='Đang xử lý', max_length=50, verbose_name='Trạng thái'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Tên tài khoản'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category', verbose_name='Danh mục sản phẩm'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='detail_description',
            field=models.TextField(blank=True, null=True, verbose_name='Miêu tả chi tiết'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(verbose_name='Có hoạt động?'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(verbose_name='Có đề xuất?'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Giá'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Hình ảnh sản phẩm'),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.TextField(verbose_name='Miêu tả ngắn'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=255, unique=True, verbose_name='Mã sản phẩm'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=160, verbose_name='Slug sản phẩm'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Tên sản phẩm'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Cập nhật'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='store.product')),
            ],
        ),
    ]